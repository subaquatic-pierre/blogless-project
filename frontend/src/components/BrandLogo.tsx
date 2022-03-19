import React from "react";

import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";

const BrandLogo: React.FC = () => {
  return (
    <Toolbar
      sx={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        mt: 2,
      }}
    >
      <Typography variant="h5">Serverless</Typography>
      <Typography variant="h5">Blog</Typography>
    </Toolbar>
  );
};

export default BrandLogo;
