import React from "react";
import DATA from "./lcode-react.json";
import LcodeRowV2 from "./LcodeRowV2";

const DataTable = ({ selectedTagIds, setSelectedTagIds, selectedLevelIds, setSelectedLevelIds }) => {


const handleClickLevelButton = (levelId) => () => {
    const updated = selectedLevelIds.find((id) => id === levelId)
      ? selectedLevelIds.filter((id) => id !== levelId)
      : [...selectedLevelIds, levelId];
    setSelectedLevelIds(updated);
  };

    const filteredByTagData =
      selectedTagIds.length > 0
        ? DATA.filter((data) =>
            //data.Tags.every((tagId) => selectedTagIds.includes(tagId))
            selectedTagIds.every((tagId) => data.Tags.includes(tagId))
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
            <LcodeRowV2
              id={l.Number}
              level={l.Level}
              title={l.Title}
              url={l.Url}
              tags={l.Tags}
              memo={l.Memo}
              date={l.Date}
              tagList={selectedTagIds}
              onClickTagButton={handleClickLevelButton}
              onClickLevelButton={handleClickLevelButton(l.Level)}
            />
          ))}
        </tbody>
      </table>
    );
  };

  export default DataTable;
