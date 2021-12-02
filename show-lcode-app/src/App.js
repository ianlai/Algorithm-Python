import React from "react";
import logo from "./logo.svg";
import "./App.css";
import LcodeRow from "./LcodeRow.js";
import lcodeData from "./lcodePure.json";

function LoadJson(){
    //lcodeData = JSON.parse(lcode_data);
    //console.log(lcodeData);
    console.log(lcodeData);
}
function App() {
  // 　const { lcodes } = this.state;
  LoadJson();
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Lcode list read from <code>lcode.json</code>. Happy coding :)
        </p>
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
            {
                lcodeData.map(l =>(
                    <LcodeRow id={l.Number}
                    title = {l.Title}
                    url = {l.Url}
                    tags = {l.Tags}
                    memo = {l.Memo}
                    />
                ))
            }


          {/* <LcodeRow
            id={"0123"}
            title={"Ya this is title"}
            url={"http://www.google.com"}
            tags={["BFS", "Graph"]}
            memo={"xxx"}
          />
          <LcodeRow
            id={"1156"}
            title={"Ya this is title2"}
            url={"https://leetcode.com/"}
            tags={["Heap", "Binary Search"]}
            memo={"yyyyyyyyyyyy"}
          /> */}
          </tbody>
        </table>
      </header>
    </div>
  );
}

export default App;
