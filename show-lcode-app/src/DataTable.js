import React, { useState } from "react";
import DATA from "./lcode-react.json";
import LcodeRowV2 from "./LcodeRowV2";

const DataTable = ({
  selectedTagIds,
  setSelectedTagIds,
  selectedLevelIds,
  setSelectedLevelIds,
  isHide,
  isHideStar
}) => {
  const SORT_BY = {
    ID_ASC: 1,
    ID_DESC: 2,
    DATE_ASC: 3,
    DATE_DESC: 4,
  };

  const [sortBy, setSortBy] = useState(SORT_BY.ID_ASC);

  const handleClickSortById = () => {
    if (sortBy !== SORT_BY.ID_ASC) {
      setSortBy(SORT_BY.ID_ASC);
    } else {
      setSortBy(SORT_BY.ID_DESC);
    }
  };

  const handleClickSortByDate = () => {
    if (sortBy !== SORT_BY.DATE_ASC) {
      setSortBy(SORT_BY.DATE_ASC);
    } else {
      setSortBy(SORT_BY.DATE_DESC);
    }
  };

  //Step1: filtered by tag
  const filteredByTagData =
    selectedTagIds.length > 0
      ? DATA.filter((data) =>
          //data.Tags.every((tagId) => selectedTagIds.includes(tagId))
          selectedTagIds.every((tagId) => data.Tags.includes(tagId))
        )
      : DATA;

  //Step2: filtered by tag and level 
  const filteredData =
    selectedLevelIds.length > 0
      ? filteredByTagData.filter((data) =>
          selectedLevelIds.includes(data.Level)
        )
      : filteredByTagData;

  //Step3: filtered by tag and level and sorted 
  const sortedData = filteredData.sort((a, b) => {
    if (sortBy === SORT_BY.ID_ASC) {
      if (a.Number < b.Number) return 1;
      else if (a.Number === b.Number) return 0;
      else return -1;
    } else if (sortBy === SORT_BY.ID_DESC) {
      if (a.Number > b.Number) return 1;
      else if (a.Number === b.Number) return 0;
      else return -1;
    } else if (sortBy === SORT_BY.DATE_ASC) {
      if (a.Date < b.Date) return 1;
      else if (a.Date === b.Date) return 0;
      else return -1;
    } else if (sortBy === SORT_BY.DATE_DESC) {
      if (a.Date > b.Date) return 1;
      else if (a.Date === b.Date) return 0;
      else return -1;
    }
    return null //exception
  });

  return (
    <table class="styled-table" style={{ width: "100%" }}>
      <thead>
        <tr>
          <th>
            <button class="button-sorting" onClick={handleClickSortById}>
              ID
            </button>
          </th>
          <th>Title</th>
          <th>Tags</th>
          <th>Memo</th>
          <th>
            <button class="button-sorting" onClick={handleClickSortByDate}>
              Date
            </button>
          </th>
        </tr>
      </thead>
      <tbody>
        {sortedData.map((l) => (
          <LcodeRowV2
            id={l.Number}
            level={l.Level}
            title={l.Title}
            url={l.Url}
            tags={l.Tags}
            memo={l.Memo}
            date={l.Date}
            tagList={selectedTagIds}
            
            selectedLevelIds={selectedLevelIds}
            setSelectedLevelIds={setSelectedLevelIds}
            selectedTagIds={selectedTagIds}
            setSelectedTagIds={setSelectedTagIds}

            isHide={isHide}
            isHideStar={isHideStar}
          />
        ))}
      </tbody>
    </table>
  );
};

export default DataTable;
