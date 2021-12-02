import TagButton from "./TagButton";

function LcodeRow(props) {
  return (
    <tr class="active-row">
      <th>{props.id}</th>
      <th>
          <a href={props.url} class="large-font"> {props.title} </a> 
        </th>
      <th>{
      props.tags.map(tag => (
          <TagButton name={tag}/> 
      ))
      }</th>
      <th>{props.memo}</th>
    </tr>
  );
}

export default LcodeRow;
