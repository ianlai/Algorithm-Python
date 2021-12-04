import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import LcodeRow from "./LcodeRow.js";
import FilterButton from "./FilterButton.js";
import lcodeData from "./lcode-react.json";

function LoadJson() {
  //lcodeData = JSON.parse(lcode_data);
  //console.log(lcodeData);
  console.log(lcodeData);
}
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

let shownLcodeData = lcodeData;
function filterByTags() {
  if (tagList.length === 0) {
    shownLcodeData = lcodeData;
  } else {
    shownLcodeData = [];
    for (let l of lcodeData) {
      let isIncluded = true;
      if (l.Tags.length === 0) {
        continue;
      }
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
  console.log(shownLcodeData);
}

let memberTagList, changeTagList;
let tagSet = new Set();
let tagList = [];

function App() {
  // 　const { lcodes } = this.state;
  //LoadJson();
  console.log("RERENDERING");
  console.log(tagSet);
  console.log(tagList);
  console.log("Show lcode data:", shownLcodeData.length);

  [memberTagList, changeTagList] = useState(tagList);

  let countEasy = 0,
    countMedium = 0,
    countHard = 0;
  for (let l of lcodeData) {
    if (l.Level == 1) {
      countEasy++;
    } else if (l.Level == 2) {
      countMedium++;
    } else if (l.Level == 3) {
      countHard++;
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h3>
          Lcode List parsed from <code>lcode-react.json</code>
        </h3>

        <div className="numberRow" style={{"font-weight": "bold", "font-size": "0.8em"}}>
          <span style={{ color: "#b1bee4b0" }}> {"Selected: " + shownLcodeData.length }</span>
          <span> || </span>
          <span style={{ color: "#aaaaaa" }}> {"Total: " + lcodeData.length } </span>
          <span> || </span>
          <span style={{ color: "#43e032" }}> Easy: {countEasy} </span>
          <span style={{ color: "#eecb31" }}> Medium: {countMedium} </span>
          <span style={{ color: "#e7391a" }}> Hard: {countHard} </span>
        </div>
        
        <div className="filterRow">
          {tagList.map((t) => (
            <FilterButton
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
              tagList={tagList}
              onClickTagButton={onClickTagButton}
            />
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
