import React from "react";
import axios from "axios";

import Grid from "@mui/material/Grid";

import Page from "components/Page";
import PageHeading from "components/PageHeading";
import PostCard from "components/PostCard";

import { API_DOMAIN_NAME } from "const";

const Home: React.FC = ({ children }) => {
  const [posts, setPosts] = React.useState<Post[]>([]);

  const getPosts = async () => {
    const getPostsUrl = `${API_DOMAIN_NAME}/blog`;
    const postsRes = await axios.get(getPostsUrl);
    const posts = postsRes.data;

    setPosts(posts);
  };

  React.useEffect(() => {
    getPosts();
  }, []);

  return (
    <Page>
      <PageHeading title="Home" />
      <Grid container spacing={3} sx={{ my: 1 }}>
        {posts.map((post, i) => (
          <Grid item md={4} key={i}>
            <PostCard title={post.title} postId={post.id} imageUrl="someurl" />
          </Grid>
        ))}
      </Grid>
    </Page>
  );
};

export default Home;
