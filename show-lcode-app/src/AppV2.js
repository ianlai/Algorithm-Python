import React, { useState } from "react";
import "./App.css";
import TagList from "./TagList";
import AppHeader from "./AppHeader";
import DataTable from "./DataTable";
import { ALL_TAG_LIST, ALL_LEVEL_LIST } from "./data";
import LevelList from "./LevelList";

const AppV2 = () => {

  const [selectedLevelIds, setSelectedLevelIds] = useState([]);
  const [selectedTagIds, setSelectedTagIds] = useState([]);
  const [isHide, setIsHide] = useState(false);
  const [isHideStar, setIsHideStar] = useState(false);

  console.log(
    "[App]",
    "ALL_TAG_LIST:",
    ALL_TAG_LIST,
    "ALL_LEVEL_LIST:",
    ALL_LEVEL_LIST
  );

  return (
    <div className="App">
      <AppHeader
        selectedLevelIds={selectedLevelIds}
        selectedTagIds={selectedTagIds}
      />
      <LevelList
        selectedLevelIds={selectedLevelIds}
        setSelectedLevelIds={setSelectedLevelIds}
        isHide={isHide}
        setIsHide={setIsHide}
        isHideStar={isHideStar}
        setIsHideStar={setIsHideStar}
      />
      <TagList
        selectedTagIds={selectedTagIds}
        setSelectedTagIds={setSelectedTagIds}
        isHide={isHide}
        isHideStar={isHideStar}
      />
      <DataTable
        selectedTagIds={selectedTagIds}
        setSelectedTagIds={setSelectedTagIds}
        selectedLevelIds={selectedLevelIds}
        setSelectedLevelIds={setSelectedLevelIds}
        isHide={isHide}
        isHideStar={isHideStar}
      />
    </div>
  );
};

export default AppV2;
