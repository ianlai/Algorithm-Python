import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import LcodeRow from "./LcodeRow.js";
import FilterTagButton from "./FilterTagButton.js";
import FilterLevelButton from "./FilterLevelButton.js";
import TagButton from "./TagButton";
import lcodeData from "./lcode-react.json";

// function LoadJson() {
//   //lcodeData = JSON.parse(lcode_data);
//   console.log(lcodeData);
// }
function onClickTagButton(tagName) {
  tagSet.add(tagName);
  tagList = Array.from(tagSet);
  filterByTags();
  changeTagList(tagList);
}

function onClickFilterTagButton(tagName) {
  tagSet.delete(tagName);
  tagList = Array.from(tagSet);
  filterByTags();
  changeTagList(tagList);
}

function onClickLevelButton(level) {
  levelSet.clear();
  levelSet.add(level);
  levelList = Array.from(levelSet);
  filterByTags();
  changeLevelList(levelList);
}
function onClickFilterLevelButton(level) {
  levelSet.delete(level);
  levelList = Array.from(levelSet);
  filterByTags();
  changeTagList(levelList);
}

let shownLcodeData = lcodeData;
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
    shownLcodeData = lcodeData;
  } else {
    shownLcodeData = [];
    for (let l of lcodeData) {
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

let memberTagList, changeTagList;
let memberLevelList, changeLevelList;
let allTagMap = new Map();
let allTagList = [];
let tagSet = new Set();
let tagList = [];
let levelSet = new Set([1, 2, 3]);
let levelList = [1, 2, 3];

function App() {
  console.log("RERENDERING");
  console.log(tagSet);
  console.log(tagList);
  console.log("Show lcode data:", shownLcodeData.length);

  [memberTagList, changeTagList] = useState(tagList);
  [memberLevelList, changeLevelList] = useState(levelList);

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

  allTagMap = new Map();
  for (let l of lcodeData) {
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

  return (
    <div className="App">
      <header className="App-header">
        <h3>
          Lcode List parsed from <code>lcode-react.json</code>
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
            {"Total: " + lcodeData.length}{" "}
          </span>
          {/* <span> || </span>
          <span style={{ color: "#43e032" }}> Easy: {countEasy} </span>
          <span style={{ color: "#eecb31" }}> Medium: {countMedium} </span>
          <span style={{ color: "#e7391a" }}> Hard: {countHard} </span> */}
        </div>

        <div className="LevelFilterRow">
          {levelList.map((t) => (
            <FilterLevelButton
              name={`${levelMap[t]["name"]} (${levelMap[t]["count"]})`}
              level={t}
              onClickFilterLevelButton={onClickFilterLevelButton}
            />
          ))}
        </div>

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

        <div className="TagFilterRow">
          {tagList.map((t) => (
            <FilterTagButton
              tagName={t}
              onClickFilterTagButton={onClickFilterTagButton}
            />
          ))}
        </div>
      </header>

      <table class="styled-table" style={{ width: "100%" }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Tags</th>
            <th>Memo</th>
            <th>Date</th>
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
    </div>
  );
}

export default App;
