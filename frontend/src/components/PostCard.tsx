import React from "react";

import axios, { AxiosResponse } from "axios";

import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import { useNavigate } from "react-router";

import useNotificationContext from "hooks/useNotificationContext";
import { API_DOMAIN_NAME } from "const";
import parseResponse from "utils/parseResponse";

interface PostCardProps {
  title: string;
  postId: string;
  imageUrl: string;
}

const PostCard: React.FC<PostCardProps> = ({ title, imageUrl, postId }) => {
  const [_, { setWarning, setSuccess }] = useNotificationContext();

  const navigate = useNavigate();

  const handleDeleteButtonClick = async () => {
    const deletePostUrl = `${API_DOMAIN_NAME}/blog/${postId}`;

    try {
      const res = await axios.delete(deletePostUrl);

      const error = parseResponse(res);

      if (error) {
        setWarning(error);
      } else {
        setSuccess("Post successfully deleted");
        setTimeout(() => {
          window.location.reload();
        }, 2000);
      }

      return res;
    } catch (error) {
      setWarning(error.message);
    }
  };

  return (
    <Card>
      <CardMedia
        component="img"
        height="140"
        image={imageUrl}
        alt="green iguana"
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          {title}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Lizards are a widespread group of squamate reptiles, with over 6,000
          species, ranging across all continents except Antarctica
        </Typography>
      </CardContent>
      <CardActions>
        <Button onClick={() => navigate(`/blog/${postId}`)} size="small">
          View
        </Button>
        <Button onClick={() => navigate(`/blog/${postId}/edit`)} size="small">
          Edit
        </Button>
        <Button onClick={handleDeleteButtonClick} size="small">
          Delete
        </Button>
      </CardActions>
    </Card>
  );
};

export default PostCard;
