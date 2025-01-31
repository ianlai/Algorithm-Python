import React, { useState, useEffect } from "react";
import "./App.css";
import LcodeRow from "./LcodeRow.js";
import FilterTagButton from "./FilterTagButton.js";
import FilterLevelButton from "./FilterLevelButton.js";
import TagButton from "./TagButton";
import DATA from "./lcode-react.json";

const SORT_BY = {
  ID_ASC: 1,
  ID_DESC: 2,
  DATE_ASC: 3,
  DATE_DESC: 4
};

//Add tag into filtered tag list
function onClickTagButton(targetTag) {
  if (!tagList.includes(targetTag)) {
    tagList.push(targetTag);
    filterData();
    setTagList(Array.from(tagList));
  }
}

//Remove tag from filtered tag list
function onClickFilterTagButton(targetTag) {
  tagList = tagList.filter((tag) => tag !== targetTag);
  filterData();
  setTagList(tagList);
}

//Keep only the target level
function onClickLevelButton(targetLevel) {
  levelList = [targetLevel];
  filterData();
  setLevelList(Array.from(levelList));
}

//Remove level from filtered level list
function onClickFilterLevelButton(targetLevel) {
  levelList = Array.from(levelList);
  levelList = levelList.filter((level) => level !== targetLevel);
  filterData();
  setLevelList(levelList);
}

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

function filterData() {
  console.log("[filterData]", "tagList:", tagList, "levelList:", levelList);
  if (tagList.length === 0 && levelList.length === 3) {
    console.log("Reset the data");
    shownLcodeData = DATA;
  } else {
    shownLcodeData = [];
    for (let l of DATA) {
      //Filter by Level
      if (!levelList.includes(l.Level)) {
        continue;
      }

      //Filter by Tags
      let isIncluded = true;
      //   if (l.Tags.length === 0) {
      //     continue;
      //   }
      for (let filteredTag of tagList) {
        if (!l.Tags.includes(filteredTag)) {
          isIncluded = false;
          break;
        }
      }
      if (isIncluded === true) {
        shownLcodeData.push(l);
      }
    }
  }
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

const AppHeader = () => (
  <header className="App-header">
    <h3>
      Lcode visualization parsed from <code>lcode-react.json</code>
    </h3>
    <div
      className="numberRow"
      style={{ "font-weight": "bold", "font-size": "0.8em" }}
    >
      <span style={{ color: "rgb(138 166 229)" }}>
        {" "}
        {"Selected: " + shownLcodeData.length}
      </span>
      <span> || </span>
      <span style={{ color: "rgb(138 166 229)" }}>
        {" "}
        {"Total: " + DATA.length}{" "}
      </span>
    </div>
  </header>
);

const LevelSectionAll = () => {
  console.log("[LevelSectionAll]", levelMap);
  return (
    <div className="LevelFilterRow">
      {levelList.map((t) => (
        <FilterLevelButton
          name={`${levelMap[t]["name"]} (${levelMap[t]["count"]})`}
          level={t}
          onClickFilterLevelButton={onClickFilterLevelButton}
        />
      ))}
    </div>
  );
};

const TagSectionAll = () => (
  <div className="TagFilterRowAll">
    {allTagList.map((t) => (
      <TagButton
        isSelected={false}
        isAllTag={true}
        tagName={t}
        showName={t + "(" + allTagMap.get(t) + ")"}
        onClickTagButton={onClickTagButton}
      />
    ))}
  </div>
);

const TagSectionSelected = () => {
  console.log("TagSectionSelected:", tagList);
  return (
    <div className="TagFilterRow">
      {tagList.map((t) => (
        <FilterTagButton
          tagName={t}
          onClickFilterTagButton={onClickFilterTagButton}
        />
      ))}
    </div>
  );
};

const DataTable = () => {
  return (
    <table class="styled-table" style={{ width: "100%" }}>
      <thead>
        <tr>
          <th>
            <button class="button-sorting" onClick={onClickSortById}>
              ID
            </button>
          </th>
          <th>Title</th>
          <th>Tags</th>
          <th>Memo</th>
          <th>
            <button class="button-sorting" onClick={onClickSortByDate}>
              Date
            </button>
          </th>
        </tr>
      </thead>
      <tbody>
        {shownLcodeData.map((l) => (
          <LcodeRow
            id={l.Number}
            level={l.Level}
            title={l.Title}
            url={l.Url}
            tags={l.Tags}
            memo={l.Memo}
            date={l.Date}
            tagList={tagList}
            onClickTagButton={onClickTagButton}
            onClickLevelButton={onClickLevelButton}
          />
        ))}
      </tbody>
    </table>
  );
};

//Global data
let shownLcodeData = DATA;
let allTagMap = new Map();
let allTagList = [];
let allLevelList = [1, 2, 3];
let levelMap = {
  1: {
    name: "Easy",
    count: 0
  },
  2: {
    name: "Medium",
    count: 0
  },
  3: {
    name: "Hard",
    count: 0
  }
};

//Filtered data
let tagList = [];
let setTagList;
let levelList = Array.from(allLevelList);
let setLevelList;
let sortedBy = 0;
let setSortedBy;

const App = () => {
  [tagList, setTagList] = useState(tagList);
  [levelList, setLevelList] = useState(levelList);
  [sortedBy, setSortedBy] = useState(sortedBy);
  useEffect(() => {
    console.log("useEffect");
    for (let l of DATA) {
      levelMap[l.Level]["count"] += 1;
      for (let tag of l.Tags) {
        if (allTagMap.has(tag)) {
          //can't do allTagMap[key] = value, otherwise the map size won't change
          //then the array can't be created
          allTagMap.set(tag, allTagMap.get(tag) + 1);
        } else {
          allTagMap.set(tag, 1);
        }
      }
    }
    allTagList = Array.from(allTagMap.keys());
    allTagList.sort();
  }, []);

  console.log(
    "[App]",
    "tagList:",
    tagList,
    "levelList:",
    levelList,
    "allTagMap:",
    allTagMap,
    "allLevelList:",
    allLevelList,
    "allTagList:",
    allTagList
  );

  return (
    <div className="App">
      <AppHeader />
      <LevelSectionAll />
      <TagSectionAll />
      <TagSectionSelected />
      <DataTable />
    </div>
  );
};

export default App;
