import React from "react";

import Box from "@mui/material/Box";
import Button from "@mui/material/Button";

import Page from "components/Page";
import PageHeading from "components/PageHeading";
import Heading from "components/Heading";

import { createReactEditorJS } from "react-editor-js";

const ReactEditorJS = createReactEditorJS();

const Create = () => {
  const editorCore = React.useRef(null);

  const handleInitialize = React.useCallback((instance) => {
    editorCore.current = instance;
  }, []);

  const handleSave = React.useCallback(async () => {
    const savedData = await editorCore.current.save();
    console.log(savedData);
  }, []);

  return (
    <Page>
      <PageHeading title="Create Post" />
      <Box sx={{ my: 2 }}>
        <Heading title="Editor JS"></Heading>
        <Box>
          <ReactEditorJS defaultValue={[]} onInitialize={handleInitialize} />
        </Box>
      </Box>
      <Box>
        <Button variant="contained" onClick={handleSave}>
          Save
        </Button>
      </Box>
    </Page>
  );
};

export default Create;
