import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import LcodeRow from "./LcodeRow.js";
import FilterButton from "./FilterButton.js";
import lcodeData from "./lcodePure.json";

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

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Lcode list read from <code>lcode.json</code>. Happy coding :)
        </p>

        <div className="filterRow">
          {tagList.map((t) => (
            <FilterButton
              tagName={t}
              onClickFilterTagButton={onClickFilterTagButton}
            />
          ))}
        </div>

        <div className="numberRow">
          {shownLcodeData.length + " / " + lcodeData.length}
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
                title={l.Title}
                url={l.Url}
                tags={l.Tags}
                memo={l.Memo}
                onClickTagButton={onClickTagButton}
              />
            ))}
          </tbody>
        </table>
    </div>
  );
}

export default App;
