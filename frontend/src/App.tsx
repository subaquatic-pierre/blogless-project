import React from "react";

import { createTheme, ThemeProvider } from "@mui/material/styles";
import { BrowserRouter } from "react-router-dom";
import CssBaseline from "@mui/material/CssBaseline";

import NotificationContextProvider from "context/NotificationContext";

import Layout from "layout";
import BaseRouter from "routes";

import themeOptions from "theme";

const theme = createTheme(themeOptions);

function App() {
  return (
    <BrowserRouter>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <NotificationContextProvider>
          <Layout>
            <BaseRouter />
          </Layout>
        </NotificationContextProvider>
      </ThemeProvider>
    </BrowserRouter>
  );
}

export default App;
