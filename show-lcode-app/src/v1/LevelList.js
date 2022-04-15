import React from "react";
import { ALL_LEVEL_LIST } from "./data";
import TagButton from "./TagButtonV2";
import FilterLevelButton from "./FilterLevelButton";

const LevelList = ({ selectedLevelIds, setSelectedLevelIds }) => {

  const handleClickLevelButton = (levelId) => () => {
    const updated = selectedLevelIds.find((id) => id === levelId)
      ? selectedLevelIds.filter((id) => id !== levelId)
      : [...selectedLevelIds, levelId];
    setSelectedLevelIds(updated);
  };

  return (
    <div className="LevelFilterRow">
      <ul style={{ display: "flex", flexWrap: "wrap", listStyle: "none" }}>
        {ALL_LEVEL_LIST.map((t) => {
          const isSelected = selectedLevelIds.indexOf(t.id) !== -1;
          return(
          <FilterLevelButton
            name={t.name + " (" + t.count + ")"}
            isSelected={isSelected}
            level={t.id}
            onClickFilterLevelButton={handleClickLevelButton(t.id)}
          />)
          })}
      </ul>
    </div>
  );
};

export default LevelList;
