import LevelButton from "./xxLevelButton";
import FilterLevelButton from "./FilterLevelButton";
import TagButtonV2 from "./TagButtonV2";

function LcodeRowV2(props) {
  let selectedTagIds = props.selectedTagIds;
  let setSelectedTagIds = props.setSelectedTagIds;

  const handleTagClick = (tagId) => () => {
    const updatedSelectedTags = selectedTagIds.find(
      (targetTagId) => targetTagId === tagId
    )
      ? selectedTagIds.filter((targetTagId) => targetTagId !== tagId)
      : [...selectedTagIds, tagId];
    setSelectedTagIds(updatedSelectedTags);
  };

  let selectedLevelIds = props.selectedLevelIds;
  let setSelectedLevelIds = props.setSelectedLevelIds;

  return (
    <tr class="active-row">
      <th style={{ width: "5%" }}>
        <FilterLevelButton
          name={props.id}
          level={props.level}
          selectedLevelIds={selectedLevelIds}
          setSelectedLevelIds={setSelectedLevelIds}
        />
      </th>
      <th style={{ width: "15%" }}>
        <a href={props.url} class="large-font">
          {" "}
          {props.title}{" "}
        </a>
      </th>
      <th style={{ width: "15%" }}>
        {props.tags.sort().map((tag) => {
          if (props.isHide) {
            if (tag.startsWith("##")) return;
          }
          if (props.isHideStar) {
            if (tag.startsWith("**")) return;
          }
          const isSelected = selectedTagIds.indexOf(tag) !== -1;
          return (
            <TagButtonV2
              isSelected={isSelected}
              showName={tag}
              onClickTagButton={handleTagClick(tag)}
            />
          );
        })}
      </th>
      <th style={{ width: "50%" }}> {props.memo} </th>
      <th style={{ color: "rgb(138 166 229)", width: "8%" }}> {props.date} </th>
    </tr>
  );
}

export default LcodeRowV2;
