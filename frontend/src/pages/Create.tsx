import React from "react";

import Box from "@mui/material/Box";

import Page from "components/Page";
import PageHeading from "components/PageHeading";
import Heading from "components/Heading";

const Create = () => {
  const [quillValue, setQuillValue] = React.useState("");

  const handleEditorStateChange = (state) => {
    setQuillValue(state);
    console.log(state);
  };

  return (
    <Page>
      <PageHeading title="Create Post" />
      <Box sx={{ my: 2 }}>
        <Heading title="Editor JS"></Heading>
        <Box></Box>
      </Box>
    </Page>
  );
};

export default Create;
