import React from "react";
import { useParams } from "react-router";

import Page from "components/Page";
import axios from "axios";
import { API_DOMAIN_NAME } from "const";

const Edit = () => {
  const blogId = useParams();
  const [blogData, setBlogData] = React.useState(false);

  const fetchBlogData = async () => {
    const response = await axios.get(`${API_DOMAIN_NAME}/blog/${blogId}`);
    console.log(response);
  };

  React.useEffect(() => {
    fetchBlogData();
  }, []);
  return (
    <Page>
      {blogData ? (
        <div>{JSON.stringify(blogData)}</div>
      ) : (
        <div>Loading ...</div>
      )}
    </Page>
  );
};

export default Edit;
