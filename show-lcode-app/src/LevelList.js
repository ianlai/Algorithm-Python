import React from "react";
import { ALL_LEVEL_LIST } from "./data";
import TagButton from "./TagButtonV2";
import FilterLevelButton from "./FilterLevelButton";

const LevelList = ({
  selectedLevelIds,
  setSelectedLevelIds,
  isHide,
  setIsHide,
  isHideStar,
  setIsHideStar,
}) => {
  return (
    <div className="LevelFilterRow">
      <ul
        style={{
          display: "flex",
          justifyContent: "center",
          margin: 0,
          padding: 0,
        }}
      >
        {ALL_LEVEL_LIST.map((t) => {
          const isSelected = selectedLevelIds.indexOf(t.id) !== -1;
          return (
            <FilterLevelButton
              name={t.name + " (" + t.count + ")"}
              //isSelected={isSelected}
              level={t.id}
              selectedLevelIds={selectedLevelIds}
              setSelectedLevelIds={setSelectedLevelIds}
            />
          );
        })}
        <button
          onClick={() => {
            setIsHide(!isHide);
          }}
          className = {isHide === true ? "button button-hide" : "button button-show"}
        > 
          {isHide === true ? "Hide ##" : "Show ##"}
        </button>
        <button
          onClick={() => {
            setIsHideStar(!isHideStar);
          }}
          className = {isHideStar === true ? "button button-hide" : "button button-show"}
        > 
          {isHideStar === true ? "Hide **" : "Show **"}
        </button>
      </ul>
    </div>
  );
};

export default LevelList;
