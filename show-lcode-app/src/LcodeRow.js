import TagButton from "./TagButton";

function LcodeRow(props) {
  return (
    <tr class="active-row">
      <th>{props.id}</th>
      <th style={{width:"20%"}}>
        <a href={props.url} class="large-font">
          {" "}
          {props.title}{" "}
        </a>
      </th>
      <th>
        {props.tags.map((tag) => (
          <TagButton tagName={tag} onClickTagButton={props.onClickTagButton} />
        ))}
      </th>
      <th style={{width:"50%"}}> {props.memo} </th>
    </tr>
  );
}

export default LcodeRow;
