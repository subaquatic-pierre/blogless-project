import React from "react";

import { createReactEditorJS } from "react-editor-js";
import { Formik, Field, Form, FormikHelpers, useFormik } from "formik";
import * as yup from "yup";

import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Paper from "@mui/material/Paper";
import TextField from "@mui/material/TextField";
import Stack from "@mui/material/Stack";

import Page from "components/Page";
import PageHeading from "components/PageHeading";
import Heading from "components/Heading";

import { EDITOR_JS_TOOLS } from "tools";

const ReactEditorJS = createReactEditorJS();

interface IFormValues {
  title: string;
}

const initialValues: IFormValues = {
  title: "",
};

const validationSchema = yup.object({
  title: yup.string().required("Title is required"),
});

const Create = () => {
  const editorCore = React.useRef(null);

  const handleFormSubmit = async (values: IFormValues) => {
    const formData = values;
    const contentData = await editorCore.current.save();
    console.log(JSON.stringify({ formData, contentData }, null, 2));
  };

  const formik = useFormik({
    initialValues,
    validationSchema: validationSchema,
    onSubmit: handleFormSubmit,
  });

  const handleInitialize = React.useCallback((instance) => {
    editorCore.current = instance;
  }, []);

  return (
    <Page>
      <PageHeading title="Create Post" />
      <Paper sx={{ my: 2, p: 2 }}>
        <form onSubmit={formik.handleSubmit}>
          <Stack spacing={2}>
            <TextField
              fullWidth
              id="title"
              name="title"
              label="Blog Title"
              value={formik.values.title}
              onChange={formik.handleChange}
              error={formik.touched.title && Boolean(formik.errors.title)}
              helperText={formik.touched.title && formik.errors.title}
            />
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

export default Create;
