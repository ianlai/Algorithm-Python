import React from "react";
import { ALL_TAG_LIST } from "./data";
import FilterTagButton from "./FilterTagButton";
import TagButtonV2 from "./TagButtonV2";

const TagList = ({ selectedTagIds, setSelectedTagIds, isHide, isHideStar }) => {
  const handleClick = (tagId) => () => {
    const updatedSelectedTags = selectedTagIds.find(
      (targetTagId) => targetTagId === tagId
    )
      ? selectedTagIds.filter((targetTagId) => targetTagId !== tagId)
      : [...selectedTagIds, tagId];

    setSelectedTagIds(updatedSelectedTags);
  };
  return (
    <ul
      style={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        listStyle: "none",
        margin: 0,
        padding: 0,
      }}
    >
      {ALL_TAG_LIST.map((tag) => {
        if (isHide) {
          if (tag.id.startsWith("##")) return;
        }
        if (isHideStar) {
          if (tag.id.startsWith("**")) return;
        }
        const isSelected = selectedTagIds.indexOf(tag.id) !== -1;
        return (
          <div className="TagFilterRowAll">
            <li key={tag.id}>
              <TagButtonV2
                type={"all"}
                isSelected={isSelected}
                // isAllTag={true}
                // tagName={tag.id}
                showName={tag.id + "(" + tag.count + ")"}
                // onClickTagButton={onClickTagButton}
                onClickTagButton={handleClick(tag.id)}
              />
            </li>
          </div>
        );
      })}
    </ul>
  );
};

export default TagList;
