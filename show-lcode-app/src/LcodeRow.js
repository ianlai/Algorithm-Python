import TagButton from "./TagButton";
import LevelButton from "./LevelButton";

function LcodeRow(props) {
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
                onClickTagButton={props.onClickTagButton}
              />
            );
          } else {
            return (
              <TagButton
                tagName={tag}
                onClickTagButton={props.onClickTagButton}
              />
            );
          }
        })}
      </th>
      <th style={{ width: "50%" }}> {props.memo} </th>
    </tr>
  );
}

export default LcodeRow;
