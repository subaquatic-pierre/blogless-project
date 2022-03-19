import React from "react";
import AppBar from "@mui/material/AppBar";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import Toolbar from "@mui/material/Toolbar";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";

import UserLogo from "components/UserLogo";

import useNotificationContext from "hooks/useNotificationContext";

interface ITopNavProps {
  drawerWidth: number;
  handleDrawerToggle: () => void;
}

const TopNav: React.FC<ITopNavProps> = ({
  drawerWidth,
  handleDrawerToggle,
}) => {
  const [correctNetwork, setCorrectNetwork] = React.useState(false);
  const [walletAddress, setWalletAddress] = React.useState("");
  const [_n, { setWarning }] = useNotificationContext();

  const displayTopNavItems = () => {
    return (
      <Button onClick={() => {}} variant="contained">
        LOGIN
      </Button>
    );
  };

  return (
    <>
      <AppBar
        position="fixed"
        sx={{
          width: { sm: `calc(100% - ${drawerWidth}px)` },
          ml: { sm: `${drawerWidth}px` },
        }}
        elevation={0}
        color="transparent"
      >
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            sx={{ display: { sm: "none" } }}
          >
            <MenuIcon />
          </IconButton>
          <Box sx={{ ml: "auto", display: { xs: "none", sm: "flex" } }}>
            {displayTopNavItems()}
          </Box>
        </Toolbar>
      </AppBar>
    </>
  );
};

export default TopNav;
