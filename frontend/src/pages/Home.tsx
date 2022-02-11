import React from "react";

import HomeComponent from "components/Home";
import { Container } from "@mui/material";

const Home: React.FC = ({ children }) => {
  return (
    <Container>
      <HomeComponent />
    </Container>
  );
};

export default Home;
