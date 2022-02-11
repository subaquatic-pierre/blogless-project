import React from "react";

import Box from "@mui/material/Box";

const Layout: React.FC = ({ children }) => {
  return <Box sx={{ display: "flex" }}>{children}</Box>;
};

export default Layout;
