import TagButton from "./TagButton";
import LevelButton from "./LevelButton";

function LcodeRow(props) {

    // const handleClickTagButton = (tagId) => () => {
    //     const updatedSelectedTags = selectedTagIds.find(
    //       (targetTagId) => targetTagId === tagId
    //     )
    //       ? selectedTagIds.filter((targetTagId) => targetTagId !== tagId)
    //       : [...selectedTagIds, tagId];
    //     setSelectedTagIds(updatedSelectedTags);
    //   };

  return (
    <tr class="active-row">
      <th>
        <LevelButton
          id={props.id}
          level={props.level}
          onClickLevelButton={props.onClickLevelButton}
        ></LevelButton>
      </th>
      <th style={{ width: "20%" }}>
        <a href={props.url} class="large-font">
          {" "}
          {props.title}{" "}
        </a>
      </th>
      <th>
        {props.tags.map((tag) => {
          //console.log(tag + props.tagList);
          if (props.tagList.includes(tag)) {
            console.log(tag + "is contained in tagList: " + props.tagList);
            return (
              <TagButton
                isSelected
                tagName={tag}
                showName={tag}
                onClickTagButton={props.onClickTagButton}
              />
            );
          } else {
            return (
              <TagButton
                tagName={tag}
                showName={tag}
                onClickTagButton={props.onClickTagButton}
              />
            );
          }
        })}
      </th>
      <th style={{ width: "50%" }}> {props.memo} </th>
      <th style={{ color: "rgb(138 166 229)", width: "8%" }}> {props.date} </th>
    </tr>
  );
}

export default LcodeRow;
