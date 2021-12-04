import TagButton from "./TagButton";

function LcodeRow(props) {
    let classNameLevel;
    if(props.level == 1){
        classNameLevel = "table-block-easy";
    }else if(props.level == 2){
        classNameLevel = "table-block-medium";
    }else if(props.level == 3){
        classNameLevel = "table-block-hard";
    }

  return (
    
    <tr class="active-row">
      <th className = {classNameLevel}>
          {props.id}</th>
      <th style={{width:"20%"}}>
        <a href={props.url} class="large-font">
          {" "}
          {props.title}{" "}
        </a>
      </th>
      <th>
        {props.tags.map(
            (tag) => {
                //console.log(tag + props.tagList);
                if(props.tagList.includes(tag)){
                    console.log(tag + "is contained in tagList: " + props.tagList)
                    return (<TagButton isSelected tagName={tag} onClickTagButton={props.onClickTagButton} />)
                }else{
                    return (<TagButton tagName={tag} onClickTagButton={props.onClickTagButton} />)
                }
            }
        )}
      </th>
      <th style={{width:"50%"}}> {props.memo} </th>
    </tr>
  );
}

export default LcodeRow;
