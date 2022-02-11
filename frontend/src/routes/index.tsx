import React from "react";
import { Route, Routes } from "react-router-dom";

import Home from "pages/Home";

const BaseRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  );
};

export default BaseRouter;
