import React from "react";
import logo from "./logo.svg";
import "./App.css";
import LcodeRow from "./LcodeRow.js";

function App() {
  // 　const { lcodes } = this.state;
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
          <LcodeRow
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
          />
          </tbody>
        </table>
      </header>
    </div>
  );
}

export default App;
