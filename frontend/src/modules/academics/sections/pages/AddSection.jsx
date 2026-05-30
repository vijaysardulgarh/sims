// ============================================
// ADD SECTION
// File: AddSection.jsx
// ============================================

import {
  useState,
  useEffect
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import SectionForm from "../components/SectionForm";

import sectionService from "../services/sectionService";

import classService from "../../classes/services/classService";

import mediumService from "../../mediums/services/mediumService";

import streamService from "../../streams/services/streamService";

import classroomService from "../../../infrastructure/classrooms/services/classroomService";


const AddSection = () => {

  const navigate = useNavigate();

  const [loading, setLoading] =
    useState(false);

  const [classes, setClasses] =
    useState([]);

  const [mediums, setMediums] =
    useState([]);

  const [streams, setStreams] =
    useState([]);

  const [classrooms, setClassrooms] =
    useState([]);

  // ============================================
  // LOAD DATA
  // ============================================

  useEffect(() => {

    loadData();

  }, []);

  const loadData = async () => {

    try {

      const [

        classesResponse,

        mediumsResponse,

        streamsResponse,

        classroomsResponse,

      ] = await Promise.all([

        classService.getClasses(),

        mediumService.getMediums(),

        streamService.getStreams(),

        classroomService.getClassrooms(),
      ]);

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
        "Failed to load form data"
      );
    }
  };

  // ============================================
  // CREATE SECTION
  // ============================================

  const handleSubmit = async (
    data
  ) => {

    try {

      setLoading(true);

      await sectionService.createSection(
        data
      );

      toast.success(
        "Section created successfully"
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

          : "Failed to create section"
      );

    } finally {

      setLoading(false);
    }
  };

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

          Add Section

        </h1>

        <p
          className="
            text-gray-500
            mt-1
          "
        >

          Create new section

        </p>

      </div>

      <SectionForm

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

export default AddSection;