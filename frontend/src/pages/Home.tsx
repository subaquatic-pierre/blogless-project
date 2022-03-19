import React from "react";

import Page from "components/Page";
import PageHeading from "components/PageHeading";

const Home: React.FC = ({ children }) => {
  return (
    <Page>
      <PageHeading title="Home" />
    </Page>
  );
};

export default Home;
