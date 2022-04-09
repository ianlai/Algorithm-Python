import React from "react";
import DATA from "./lcode-react.json";
import LcodeRow from "./LcodeRow.js";

const DataTable = ({ selectedTagIds, selectedLevelIds }) => {

//     //Add tag into filtered tag list
//     const onClickTagButton = (targetTag) => {
//     if (!tagList.includes(targetTag)) {
//       tagList.push(targetTag);
//       //filterData();
//       setTagList(Array.from(tagList));
//     }
//   }


//   //Keep only the target level
// function onClickLevelButton(targetLevel) {
//     levelList = [targetLevel];
//     //filterData();
//     setLevelList(Array.from(levelList));
//   }

    const filteredByTagData =
      selectedTagIds.length > 0
        ? DATA.filter((data) =>
            data.Tags.some((tagId) => selectedTagIds.includes(tagId))
          )
        : DATA;
  
    const filteredData =
      selectedLevelIds.length > 0
        ? filteredByTagData.filter((data) =>
            selectedLevelIds.includes(data.Level)
          )
        : filteredByTagData;
  
    return (
      <table class="styled-table" style={{ width: "100%" }}>
        <thead>
          <tr>
            <th>
              <button class="button-sorting" onClick={null}>
                ID
              </button>
            </th>
            <th>Title</th>
            <th>Tags</th>
            <th>Memo</th>
            <th>
              <button class="button-sorting" onClick={null}>
                Date
              </button>
            </th>
          </tr>
        </thead>
        <tbody>
          {filteredData.map((l) => (
            <LcodeRow
              id={l.Number}
              level={l.Level}
              title={l.Title}
              url={l.Url}
              tags={l.Tags}
              memo={l.Memo}
              date={l.Date}
              tagList={selectedTagIds}
              //onClickTagButton={onClickTagButton}
              //onClickLevelButton={onClickLevelButton}
            />
          ))}
        </tbody>
      </table>
    );
  };

  export default DataTable;
