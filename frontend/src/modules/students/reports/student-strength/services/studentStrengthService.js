import api from "../../../../../services/api/axios";

const getStudentStrength = async () => {

  const response =
    await api.get(
      "/students/reports/student-strength/"
    );

  return response.data;
};

const downloadExcel = async () => {

  return await api.get(

    "/students/reports/student-strength/excel/",

    {
      responseType: "blob",
    }

  );

};

const downloadPdf = async () => {

  return await api.get(

    "/students/reports/student-strength/pdf/",

    {
      responseType: "blob",
    }

  );

};

export default {

  getStudentStrength,

  downloadExcel,

  downloadPdf,

};