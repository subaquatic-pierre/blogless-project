import React from "react";

import { createReactEditorJS } from "react-editor-js";
import { Formik, Field, Form, FormikHelpers } from "formik";

import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Paper from "@mui/material/Paper";
import TextField from "@mui/material/TextField";

import Page from "components/Page";
import PageHeading from "components/PageHeading";
import Heading from "components/Heading";

import { EDITOR_JS_TOOLS } from "tools";

const ReactEditorJS = createReactEditorJS();

interface IFormValues {
  title: string;
}

const initialFormValues: IFormValues = {
  title: "",
};

const Create = () => {
  const editorCore = React.useRef(null);
  const [submitting, setSubmitting] = React.useState(false);

  const handleInitialize = React.useCallback((instance) => {
    editorCore.current = instance;
  }, []);

  const handleSave = React.useCallback(async () => {
    const savedData = await editorCore.current.save();
    console.log(savedData);
  }, []);

  const handleFormSubmit = (values: IFormValues) => {
    setTimeout(() => {
      alert(JSON.stringify(values, null, 2));
      setSubmitting(false);
    }, 500);
  };

  return (
    <Page>
      <PageHeading title="Create Post" />
      <Paper sx={{ my: 2, p: 2 }}>
        <Formik initialValues={initialFormValues} onSubmit={handleFormSubmit}>
          <Form>
            <TextField
              id="outlined-basic"
              label="Outlined"
              variant="outlined"
            />

            <button type="submit">Submit</button>
          </Form>
        </Formik>
        <Box sx={{ my: 2 }}>
          <ReactEditorJS
            defaultValue={[]}
            onInitialize={handleInitialize}
            tools={EDITOR_JS_TOOLS}
          />
        </Box>
      </Paper>
      <Box>
        <Button variant="contained" onClick={handleSave}>
          Save
        </Button>
      </Box>
    </Page>
  );
};

export default Create;
