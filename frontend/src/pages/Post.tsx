import React from "react";
import { useParams } from "react-router";
import { useNavigate } from "react-router-dom";
import parseResponse from "utils/parseResponse";

import Page from "components/Page";
import axios from "axios";
import { API_DOMAIN_NAME } from "const";
import useNotificationContext from "hooks/useNotificationContext";

const Post = () => {
  const { id } = useParams();
  const [_, { setWarning }] = useNotificationContext();

  const [blogData, setBlogData] = React.useState(false);

  const fetchBlogData = async () => {
    const url = `${API_DOMAIN_NAME}/blog/${id}`;
    const response = await axios.get(url);

    const error = parseResponse(response);

    if (error) {
      setWarning(error);
    } else {
      setBlogData(response.data);
    }
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

export default Post;
