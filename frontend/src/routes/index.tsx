import React from "react";
import { Route, Routes } from "react-router-dom";

import Home from "pages/Home";
import Create from "pages/Create";
import Edit from "pages/Edit";
import Post from "pages/Post";

const BaseRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/create" element={<Create />} />
      <Route path="/blog/:id/edit" element={<Edit />} />
      <Route path="/blog/:id" element={<Post />} />
    </Routes>
  );
};

export default BaseRouter;
