import React from "react";

import Typography from "@mui/material/Typography";

interface HeadingProps {
  title: string;
}

const Heading: React.FC<HeadingProps> = ({ title }) => {
  return <Typography variant="h3">{title}</Typography>;
};

export default Heading;
