import React from "react";

import Box from "@mui/material/Box";

import Heading from "components/Heading";

interface PageHeadingProps {
  title: string;
}

const PageHeading: React.FC<PageHeadingProps> = ({ title }) => {
  return (
    <Box sx={{ display: "flex", justifyContent: "center" }}>
      <Heading title={title} />
    </Box>
  );
};

export default PageHeading;
