import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";
import LcodeRow from "./LcodeRow.js";
import FilterTagButton from "./FilterTagButton.js";
import FilterLevelButton from "./FilterLevelButton.js";
import TagButton from "./TagButton";
import LCODEDATAS from "./lcode-react.json";

function onClickTagButton(tagName) {
  tagSet.add(tagName);
  tagList = Array.from(tagSet);
  filterByTags();
  setTagList(tagList);
}

function onClickFilterTagButton(tagName) {
  tagSet.delete(tagName);
  tagList = Array.from(tagSet);
  filterByTags();
  setTagList(tagList);
}

function onClickLevelButton(level) {
  levelSet.clear();
  levelSet.add(level);
  levelList = Array.from(levelSet);
  filterByTags();
  setLevelList(levelList);
}
function onClickFilterLevelButton(level) {
  levelSet.delete(level);
  levelList = Array.from(levelSet);
  filterByTags();
  setTagList(levelList);
}

let shownLcodeData = LCODEDATAS;
function filterByTags() {
  console.log(
    "filterByTags:",
    tagList,
    tagList.length,
    levelSet,
    levelSet.size
  );
  if (tagList.length === 0 && levelSet.size === 3) {
    console.log("Reset data");
    shownLcodeData = LCODEDATAS;
  } else {
    shownLcodeData = [];
    for (let l of LCODEDATAS) {
      //Level
      if (levelSet.size !== 3 && !levelSet.has(l.Level)) {
        continue;
      }

      //Tags
      let isIncluded = true;
      //   if (l.Tags.length === 0) {
      //     continue;
      //   }
      for (let filteredTag of tagSet) {
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
  //   console.log(shownLcodeData);
}
function sortList() {
  if (sortedBy == 0) {
    shownLcodeData.sort((a, b) => {
      if (a.Number > b.Number) return 1;
      else if (a.Number == b.Number) return 0;
      else return -1;
    });
  } else if (sortedBy == 1) {
    shownLcodeData.sort((a, b) => {
      if (a.Date > b.Date) return 1;
      else if (a.Date == b.Date) return 0;
      else return -1;
    });
  } else if (sortedBy == 2) {
    shownLcodeData.sort((a, b) => {
      if (a.Date > b.Date) return -1;
      else if (a.Date == b.Date) return 0;
      else return 1;
    });
  }
  //console.log(shownLcodeData);
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
        {"Total: " + LCODEDATAS.length}{" "}
      </span>
    </div>
  </header>
);

const LevelSectionAll = () => (
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

const TagSectionSelected = () => (
  <div className="TagFilterRow">
    {tagList.map((t) => (
      <FilterTagButton
        tagName={t}
        onClickFilterTagButton={onClickFilterTagButton}
      />
    ))}
  </div>
);

const DataTable = () => {
  return (
    <table class="styled-table" style={{ width: "100%" }}>
      <thead>
        <tr>
          <th>
            <button
              class="button-sorting"
              onClick={() => {
                sortedBy = 0;
                sortList();
              }}
            >
              ID
            </button>
          </th>
          <th>Title</th>
          <th>Tags</th>
          <th>Memo</th>
          <th>
            <button
              class="button-sorting"
              onClick={() => {
                if (sortedBy == 0) {
                  sortedBy = 1;
                } else if (sortedBy == 1) {
                  sortedBy = 2;
                } else if (sortedBy == 2) {
                  sortedBy = 1;
                }
                sortList();
              }}
            >
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

let memberTagList, setTagList;
let memberLevelList, setLevelList;
let sortedBy = 0,
  setSortedBy;
let allTagMap = new Map();
let allTagList = [];
let tagSet = new Set();
let tagList = [];
let levelSet = new Set([1, 2, 3]);
let levelList = [1, 2, 3];
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

const App = () => {
  console.log(tagSet);
  console.log(tagList);
  console.log("Show lcode data:", shownLcodeData.length);

  [memberTagList, setTagList] = useState(tagList);
  [memberLevelList, setLevelList] = useState(levelList);
  [memberLevelList, setSortedBy] = useState(sortedBy);

  useEffect(() => {
    console.log("useEffect");
    allTagMap = new Map();
    for (let l of LCODEDATAS) {
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
    console.log("allTagMap:", allTagMap);
    console.log("allTagList:", allTagList);
  }, []);

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
