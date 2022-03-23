import React from "react";
import { Route, Routes } from "react-router-dom";

import Home from "pages/Home";
import Create from "pages/Create";
import Edit from "pages/Edit";

const BaseRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/create" element={<Create />} />
      <Route path="/blog/:id" element={<Edit />} />
    </Routes>
  );
};

export default BaseRouter;
