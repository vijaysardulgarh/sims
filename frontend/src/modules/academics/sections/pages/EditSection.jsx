// ============================================
// EDIT SECTION
// File: EditSection.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import {
  useNavigate,
  useParams
} from "react-router-dom";

import toast from "react-hot-toast";

import SectionForm from "../components/SectionForm";

import sectionService from "../services/sectionService";

import classService from "../../classes/services/classService";

import mediumService from "../../mediums/services/mediumService";

import streamService from "../../streams/services/streamService";

import classroomService from "../../../infrastructure/classrooms/services/classroomService";


const EditSection = () => {

  const { id } = useParams();

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const [pageLoading,
    setPageLoading] =
    useState(true);

  const [initialData,
    setInitialData] =
    useState({});

  const [classes,
    setClasses] =
    useState([]);

  const [mediums,
    setMediums] =
    useState([]);

  const [streams,
    setStreams] =
    useState([]);

  const [classrooms,
    setClassrooms] =
    useState([]);

  // ============================================
  // LOAD DATA
  // ============================================

  useEffect(() => {

    loadData();

  }, [id]);

  const loadData = async () => {

    try {

      const [

        sectionResponse,

        classesResponse,

        mediumsResponse,

        streamsResponse,

        classroomsResponse

      ] = await Promise.all([

        sectionService.getSection(id),

        classService.getClasses(),

        mediumService.getMediums(),

        streamService.getStreams(),

        classroomService.getClassrooms(),
      ]);

      console.log(
        "SECTION RESPONSE:",
        sectionResponse
      );

      setInitialData(
        sectionResponse
      );

      setClasses(
        classesResponse.results ||
        classesResponse
      );

      setMediums(
        mediumsResponse.results ||
        mediumsResponse
      );

      setStreams(
        streamsResponse.results ||
        streamsResponse
      );

      setClassrooms(
        classroomsResponse.results ||
        classroomsResponse
      );

    } catch (error) {

      console.error(error);

      toast.error(
        "Failed to load section"
      );

    } finally {

      setPageLoading(false);
    }
  };

  // ============================================
  // UPDATE SECTION
  // ============================================

  const handleSubmit = async (
    data
  ) => {

    try {

      setLoading(true);

      await sectionService.updateSection(
        id,
        data
      );

      toast.success(
        "Section updated successfully"
      );

      navigate(
        "/dashboard/academics/sections"
      );

    } catch (error) {

      console.error(error);

      toast.error(

        error.response?.data

          ? JSON.stringify(
              error.response.data
            )

          : "Update failed"
      );

    } finally {

      setLoading(false);
    }
  };

  // ============================================
  // LOADING
  // ============================================

  if (pageLoading) {

    return (

      <div className="p-6">

        Loading section...

      </div>
    );
  }

  // ============================================
  // UI
  // ============================================

  return (

    <div className="space-y-6">

      <div>

        <h1
          className="
            text-3xl
            font-bold
            text-gray-800
          "
        >

          Edit Section

        </h1>

        <p
          className="
            text-gray-500
            mt-1
          "
        >

          Update section details

        </p>

      </div>

      <SectionForm

        initialData={initialData}

        classes={classes}

        mediums={mediums}

        streams={streams}

        classrooms={classrooms}

        onSubmit={handleSubmit}

        loading={loading}
      />

    </div>
  );
};

export default EditSection;