import React from "react";
import { ALL_TAG_LIST } from "./data";
import FilterTagButton from "./FilterTagButton";
import TagButton from "./TagButtonV2";

const TagList = ({ selectedTagIds, setSelectedTagIds }) => {
  const handleClick = (tagId) => () => {
    const updatedSelectedTags = selectedTagIds.find(
      (targetTagId) => targetTagId === tagId
    )
      ? selectedTagIds.filter((targetTagId) => targetTagId !== tagId)
      : [...selectedTagIds, tagId];

    // updatedSelectedTags.sort((a, b) => {
    //     if (a.tagId > b.tagId) return 1;
    //     else if (a.tagId === b.tagId) return 0;
    //     else return -1;
    //   });
    // console.log("updatedSelectedTags:", updatedSelectedTags)
    setSelectedTagIds(updatedSelectedTags);
  };
  return (
    <ul style={{ display: "flex", flexWrap: "wrap", listStyle: "none" }}>
      {ALL_TAG_LIST.map((tag) => {
        const isSelected = selectedTagIds.indexOf(tag.id) !== -1;
        return (
          <div className="TagFilterRowAll">
            <li key={tag.id}>
              {/* <button
                onClick={handleClick(tag.id)}
                style={{ background: isSelected ? "red" : "white" }}
              >
                {tag.id} {tag.count}
              </button> */}
              <TagButton
                type = {"all"}
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
