import React from "react";

import { useTheme } from "@mui/material/styles";
import Box from "@mui/material/Box";

import AlertMessage from "components/AlertMessage";
import SideNav from "components/SideNav";
import TopNav from "components/TopNav";
import Footer from "components/Footer";

const drawerWidth = 240;

const Layout: React.FC = ({ children }) => {
  const [mobileOpen, setMobileOpen] = React.useState(false);
  const theme = useTheme();

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  return (
    <Box sx={{ display: "flex" }}>
      <TopNav
        drawerWidth={drawerWidth}
        handleDrawerToggle={handleDrawerToggle}
      />
      <SideNav
        drawerWidth={drawerWidth}
        handleDrawerToggle={handleDrawerToggle}
        mobileOpen={mobileOpen}
      />

      <Box
        sx={{
          width: "100%",
          [theme.breakpoints.up("sm")]: {
            width: { sm: `calc(100% - ${drawerWidth}px)` },
          },
          backgroundColor: theme.palette.secondary.light,
          minHeight: `100vh`,
          display: "flex",
          flexDirection: "column",
        }}
      >
        <AlertMessage />
        <Box
          sx={{
            mt: 8,
          }}
          component="main"
        >
          {children}
        </Box>
        <Footer />
      </Box>
    </Box>
  );
};

export default Layout;
