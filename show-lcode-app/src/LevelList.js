import React from "react";
import { ALL_LEVEL_LIST } from "./data";
import TagButton from "./TagButtonV2";
import FilterLevelButton from "./FilterLevelButton";

const LevelList = ({ selectedLevelIds, setSelectedLevelIds }) => {

  return (
    <div className="LevelFilterRow">
      <ul style={{ display: "flex", flexWrap: "wrap", listStyle: "none" }}>
        {ALL_LEVEL_LIST.map((t) => {
          const isSelected = selectedLevelIds.indexOf(t.id) !== -1;
          return(
          <FilterLevelButton
            name={t.name + " (" + t.count + ")"}
            //isSelected={isSelected}
            level={t.id}
            selectedLevelIds={selectedLevelIds}
            setSelectedLevelIds={setSelectedLevelIds}
          />)
          })}
      </ul>
    </div>
  );
};

export default LevelList;
