import React, { useState } from "react";
import "./App.css";
import FilterTagButton from "./FilterTagButton.js";
import DATA from "./lcode-react.json";
import TagList from "./TagList";
import AppHeader from "./AppHeader";
import DataTable from "./DataTable";
import { ALL_TAG_LIST, ALL_LEVEL_LIST } from "./data";
import LevelList from "./LevelList";

const SORT_BY = {
  ID_ASC: 1,
  ID_DESC: 2,
  DATE_ASC: 3,
  DATE_DESC: 4,
};

function onClickSortById() {
  if (sortedBy !== SORT_BY.ID_ASC) {
    sortedBy = SORT_BY.ID_ASC;
  } else {
    sortedBy = SORT_BY.ID_DESC;
  }
  sortList();
}

function onClickSortByDate() {
  if (sortedBy !== SORT_BY.DATE_ASC) {
    sortedBy = SORT_BY.DATE_ASC;
  } else {
    sortedBy = SORT_BY.DATE_DESC;
  }
  sortList();
}

function sortList() {
  if (sortedBy === SORT_BY.ID_ASC) {
    shownLcodeData.sort((a, b) => {
      if (a.Number > b.Number) return 1;
      else if (a.Number === b.Number) return 0;
      else return -1;
    });
  } else if (sortedBy === SORT_BY.ID_DESC) {
    shownLcodeData.sort((a, b) => {
      if (a.Number < b.Number) return 1;
      else if (a.Number === b.Number) return 0;
      else return -1;
    });
  } else if (sortedBy === SORT_BY.DATE_ASC) {
    shownLcodeData.sort((a, b) => {
      if (a.Date > b.Date) return 1;
      else if (a.Date === b.Date) return 0;
      else return -1;
    });
  } else if (sortedBy === SORT_BY.DATE_DESC) {
    shownLcodeData.sort((a, b) => {
      if (a.Date > b.Date) return -1;
      else if (a.Date === b.Date) return 0;
      else return 1;
    });
  }
  setSortedBy(sortedBy);
}

//Global data
let shownLcodeData = DATA;
let allTagMap = new Map();
let allTagList = [];
let allLevelList = [1, 2, 3];
let levelMap = {
  1: {
    name: "Easy",
    count: 0,
  },
  2: {
    name: "Medium",
    count: 0,
  },
  3: {
    name: "Hard",
    count: 0,
  },
};

//Filtered data
let tagList = [];
let setTagList;
let levelList = Array.from(allLevelList);
let setLevelList;
let sortedBy = 0;
let setSortedBy;

const AppV2 = () => {
  [tagList, setTagList] = useState(tagList);
  [levelList, setLevelList] = useState(levelList);
  //[sortedBy, setSortedBy] = useState(sortedBy);
  
  const [selectedLevelIds, setSelectedLevelIds] = useState([]);
  const [selectedTagIds, setSelectedTagIds] = useState([]);
  const [isHide, setIsHide] = useState(false);

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
      />
      <TagList
        selectedTagIds={selectedTagIds}
        setSelectedTagIds={setSelectedTagIds}
        isHide={isHide}
      />
      <button onClick={() => {
          setIsHide(!isHide)
      }} className={isHide === true ? "button-hide": "button-show"} >
        {isHide === true ? "Hide" : "Show" }
      </button>
      <DataTable
        selectedTagIds={selectedTagIds}
        setSelectedTagIds={setSelectedTagIds}
        selectedLevelIds={selectedLevelIds}
        setSelectedLevelIds={setSelectedLevelIds}
        isHide={isHide}
      />
    </div>
  );
};

export default AppV2;
