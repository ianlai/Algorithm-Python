import React from "react";
import { ALL_TAG_LIST } from "./data";
import TagButton from "./TagButton";

const TagList = ({ selectedTagIds, setSelectedTagIds }) => {
  const handleClick = (tagId) => () => {
    const updatedSelectedTags = selectedTagIds.find(
      (targetTagId) => targetTagId === tagId
    )
      ? selectedTagIds.filter((targetTagId) => targetTagId !== tagId)
      : [...selectedTagIds, tagId];
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
                isSelected={false}
                isAllTag={true}
                tagName={tag.id}
                showName={tag.id + "(" + tag.count + ")"}
                // onClickTagButton={onClickTagButton}
              />
            </li>
          </div>
        );
      })}
    </ul>
  );
};

export default TagList;
