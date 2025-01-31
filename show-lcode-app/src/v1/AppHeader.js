import React from "react";
import DATA from "./lcode-react.json";

const AppHeader = ({ selectedTagIds, selectedLevelIds }) => {
  const filteredByTagData =
    selectedTagIds.length > 0
      ? DATA.filter((data) =>
          selectedTagIds.every((tagId) => data.Tags.includes(tagId))
        )
      : DATA;

  const filteredData =
    selectedLevelIds.length > 0
      ? filteredByTagData.filter((data) =>
          selectedLevelIds.includes(data.Level)
        )
      : filteredByTagData;

  return (
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
          {"Selected: " + filteredData.length}
        </span>
        <span> || </span>
        <span style={{ color: "rgb(138 166 229)" }}>
          {" "}
          {"Total: " + DATA.length}{" "}
        </span>
      </div>
    </header>
  );
};

export default AppHeader;
