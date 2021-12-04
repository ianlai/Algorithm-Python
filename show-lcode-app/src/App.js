import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import LcodeRow from "./LcodeRow.js";
import lcodeData from "./lcodePure.json";

// let tagList = []
const tagSet = new Set();
let tagList = [];

function LoadJson() {
  //lcodeData = JSON.parse(lcode_data);
  //console.log(lcodeData);
  console.log(lcodeData);
}
function onClickTagButton(tagName) {
  tagSet.add(tagName);
  tagList = Array.from(tagSet);
  filterByTags();
  changePercent(tagName);
}
// function componentDidMount() {
//     this.setState({});
// }

let shownLcodeData = lcodeData;
function filterByTags() {
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
    // for(let tag of l.Tags){
    //     if(!tagSet.has(tag)){
    //         isIncluded = false;
    //         continue;
    //     }
    // }
    if (isIncluded === true) {
      shownLcodeData.push(l);
    }
  }
  console.log(shownLcodeData);
}

let percent, changePercent;

function App() {
  // 　const { lcodes } = this.state;
  //LoadJson();
  console.log("RERENDERING");
  console.log(tagSet);

  [percent, changePercent] = useState("30%");

  return (
    <div className="App">
      <header className="App-header">
        <p>
          Lcode list read from <code>lcode.json</code>. Happy coding :)
        </p>
        <div>
        {
            tagList.map((t) => (
                <button class="button-filter"> {t} </button>
                ))
        }
        </div>

        <table class="styled-table">
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
      </header>
    </div>
  );
}

export default App;
