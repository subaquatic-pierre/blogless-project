import React from "react";
import { useNavigate, useParams } from "react-router-dom";
import axios, { AxiosResponse } from "axios";
import { createReactEditorJS } from "react-editor-js";
import { useFormik } from "formik";
import * as yup from "yup";

import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Paper from "@mui/material/Paper";
import TextField from "@mui/material/TextField";
import Stack from "@mui/material/Stack";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";

import Page from "components/Page";
import PageHeading from "components/PageHeading";

import parseResponse from "utils/parseResponse";
import { API_DOMAIN_NAME } from "const";
import { EDITOR_JS_TOOLS } from "tools";
import useNotificationContext from "hooks/useNotificationContext";

const ReactEditorJS = createReactEditorJS();

interface IFormValues {
  title: string;
  category: string;
}

const initialValues: IFormValues = {
  title: "",
  category: "Blog",
};

const validationSchema = yup.object({
  title: yup.string().required("Title is required"),
  category: yup.string().required("Category is required"),
});

const Edit = () => {
  const navigate = useNavigate();
  const { id } = useParams();
  const [_, { setWarning, setSuccess }] = useNotificationContext();
  const editorCore = React.useRef(null);
  const [formValues, setFormValues] =
    React.useState<IFormValues>(initialValues);

  const sendPostRequest = async (data: any): Promise<AxiosResponse> => {
    const createPostUrl = `${API_DOMAIN_NAME}/blog`;
    try {
      const res = await axios.post(createPostUrl, data);
      return res;
    } catch (error) {
      setWarning(error.message);
    }
  };

  const handleFormSubmit = async (values: IFormValues) => {
    const metaData = values;
    const content = await editorCore.current.save();

    const form = new FormData();
    form.append("metaData", JSON.stringify(metaData));
    form.append("content", content);

    const body = JSON.stringify({ metaData, content });

    const response = await sendPostRequest(body);

    const error = parseResponse(response);

    if (error) {
      setWarning(error);
    } else {
      setSuccess("Post successfully created");
      setTimeout(() => {
        navigate("/");
      }, 2000);
    }
  };

  const formik = useFormik({
    initialValues: formValues,
    validationSchema: validationSchema,
    enableReinitialize: true,
    onSubmit: handleFormSubmit,
  });

  const handleInitialize = React.useCallback((instance) => {
    editorCore.current = instance;
  }, []);

  const fetchBlogData = async () => {
    const url = `${API_DOMAIN_NAME}/blog/${id}`;
    const response = await axios.get(url);

    const error = parseResponse(response);

    if (error) {
      setWarning(error);
    } else {
      const metaData = response.data.meta_data;
      const content = response.data.content;
      setFormValues({
        title: metaData.title,
        category: metaData.template,
      });
    }
  };

  React.useEffect(() => {
    fetchBlogData();
  }, []);

  React.useEffect(() => {
    console.log(formValues);
  }, [formValues]);
  return (
    <Page>
      <PageHeading title="Edit Post" />
      <Paper sx={{ my: 2, p: 4 }}>
        <form onSubmit={formik.handleSubmit}>
          <Stack
            spacing={4}
            sx={{
              "& .ce-block__content": {
                maxWidth: "none",
              },
            }}
          >
            <TextField
              id="title"
              name="title"
              label="Blog Title"
              variant="standard"
              value={formik.values.title}
              onChange={formik.handleChange}
              error={formik.touched.title && Boolean(formik.errors.title)}
              helperText={formik.touched.title && formik.errors.title}
            />
            <FormControl>
              <InputLabel id="category-select-label">Category</InputLabel>
              <Select
                id="category"
                name="category"
                label="Category"
                variant="standard"
                value={formik.values.category}
                onChange={formik.handleChange}
                error={
                  formik.touched.category && Boolean(formik.errors.category)
                }
              >
                <MenuItem value={"Blog"}>Blog</MenuItem>
              </Select>
            </FormControl>
            <Box sx={{ my: 2 }}>
              <ReactEditorJS
                defaultValue={[]}
                onInitialize={handleInitialize}
                tools={EDITOR_JS_TOOLS}
              />
            </Box>
            <Box
              sx={{
                display: "flex",
                flexDirection: "row",
                justifyContent: "flex-end",
              }}
            >
              <Button color="primary" variant="contained" type="submit">
                Submit
              </Button>
            </Box>
          </Stack>
        </form>
      </Paper>
    </Page>
  );
};

export default Edit;
