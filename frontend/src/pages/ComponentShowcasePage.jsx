import { useState } from "react";

import PageHeader from "../components/ui/PageHeader";
import Button from "../components/ui/Button";
import Input from "../components/ui/Input";
import Select from "../components/ui/Select";
import Textarea from "../components/ui/Textarea";
import DateInput from "../components/forms/DateInput";

import Tabs from "../components/ui/Tabs";

import CrudDrawer from "../components/crud/CrudDrawer";
import SearchBar from "../components/crud/SearchBar";
import DataTable from "../components/crud/DataTable";
import Pagination from "../components/crud/Pagination";

import FileUpload from "../components/forms/FileUpload";
import ImageUpload from "../components/forms/ImageUpload";

const StudentShowcasePage = () => {

    const [search, setSearch] =
        useState("");

    const [drawerOpen, setDrawerOpen] =
        useState(false);

    const [activeTab, setActiveTab] =
        useState("Basic Info");

    const [studentPhoto, setStudentPhoto] =
        useState(null);

    const [birthCertificate, setBirthCertificate] =
        useState(null);

    const [page, setPage] =
        useState(1);

    const [formData, setFormData] =
        useState({
            admission_no: "",
            first_name: "",
            last_name: "",
            gender: "",
            dob: "",
            class_name: "",
            section: "",
            father_name: "",
            mother_name: "",
            address: "",
        });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]:
                e.target.value,
        });
    };

    const columns = [
        {
            key: "admission_no",
            label: "Admission No",
        },
        {
            key: "name",
            label: "Student Name",
        },
        {
            key: "class_name",
            label: "Class",
        },
        {
            key: "section",
            label: "Section",
        },
        {
            key: "status",
            label: "Status",
        },
    ];

    const data = [
        {
            id: 1,
            admission_no: "ADM001",
            name: "Rahul Sharma",
            class_name: "10",
            section: "A",
            status: "Active",
        },
        {
            id: 2,
            admission_no: "ADM002",
            name: "Priya Singh",
            class_name: "9",
            section: "B",
            status: "Active",
        },
        {
            id: 3,
            admission_no: "ADM003",
            name: "Amit Kumar",
            class_name: "8",
            section: "A",
            status: "Inactive",
        },
    ];

    return (
        <div className="p-6 space-y-6">

            <PageHeader
                title="Students"
                subtitle="Student Management Showcase"
                breadcrumbs={[
                    "Dashboard",
                    "Academics",
                    "Students",
                ]}
                actions={
                    <Button
                        onClick={() =>
                            setDrawerOpen(true)
                        }
                    >
                        Add Student
                    </Button>
                }
            />

            <SearchBar
                value={search}
                onChange={setSearch}
            />

            <DataTable
                columns={columns}
                data={data}
                onView={(row) =>
                    console.log(row)
                }
                onEdit={(row) =>
                    console.log(row)
                }
                onDelete={(row) =>
                    console.log(row)
                }
            />

            <Pagination
                currentPage={page}
                totalPages={10}
                onPageChange={setPage}
            />

            <CrudDrawer
                open={drawerOpen}
                title="Add Student"
                onClose={() =>
                    setDrawerOpen(false)
                }
            >

                <Tabs
                    tabs={[
                        "Basic Info",
                        "Academic",
                        "Guardian",
                        "Documents",
                    ]}
                    activeTab={activeTab}
                    onChange={setActiveTab}
                />

                <div className="mt-6">

                    {activeTab ===
                        "Basic Info" && (
                        <div className="grid grid-cols-2 gap-4">

                            <ImageUpload
                                label="Student Photo"
                                image={
                                    studentPhoto
                                        ? URL.createObjectURL(
                                              studentPhoto
                                          )
                                        : null
                                }
                                onChange={
                                    setStudentPhoto
                                }
                            />

                            <Input
                                label="Admission No"
                                name="admission_no"
                                value={
                                    formData.admission_no
                                }
                                onChange={
                                    handleChange
                                }
                            />

                            <Input
                                label="First Name"
                                name="first_name"
                                value={
                                    formData.first_name
                                }
                                onChange={
                                    handleChange
                                }
                            />

                            <Input
                                label="Last Name"
                                name="last_name"
                                value={
                                    formData.last_name
                                }
                                onChange={
                                    handleChange
                                }
                            />

                            <Select
                                label="Gender"
                                name="gender"
                                value={
                                    formData.gender
                                }
                                onChange={
                                    handleChange
                                }
                                options={[
                                    {
                                        value:
                                            "Male",
                                        label:
                                            "Male",
                                    },
                                    {
                                        value:
                                            "Female",
                                        label:
                                            "Female",
                                    },
                                ]}
                            />

                            <DateInput
                                label="Date of Birth"
                                name="dob"
                                value={
                                    formData.dob
                                }
                                onChange={
                                    handleChange
                                }
                            />

                        </div>
                    )}

                    {activeTab ===
                        "Academic" && (
                        <div className="grid grid-cols-2 gap-4">

                            <Select
                                label="Class"
                                name="class_name"
                                value={
                                    formData.class_name
                                }
                                onChange={
                                    handleChange
                                }
                                options={[
                                    {
                                        value:
                                            "10",
                                        label:
                                            "10",
                                    },
                                    {
                                        value:
                                            "9",
                                        label:
                                            "9",
                                    },
                                ]}
                            />

                            <Select
                                label="Section"
                                name="section"
                                value={
                                    formData.section
                                }
                                onChange={
                                    handleChange
                                }
                                options={[
                                    {
                                        value:
                                            "A",
                                        label:
                                            "A",
                                    },
                                    {
                                        value:
                                            "B",
                                        label:
                                            "B",
                                    },
                                ]}
                            />

                        </div>
                    )}

                    {activeTab ===
                        "Guardian" && (
                        <div className="grid grid-cols-2 gap-4">

                            <Input
                                label="Father Name"
                                name="father_name"
                                value={
                                    formData.father_name
                                }
                                onChange={
                                    handleChange
                                }
                            />

                            <Input
                                label="Mother Name"
                                name="mother_name"
                                value={
                                    formData.mother_name
                                }
                                onChange={
                                    handleChange
                                }
                            />

                            <div className="col-span-2">

                                <Textarea
                                    label="Address"
                                    name="address"
                                    value={
                                        formData.address
                                    }
                                    onChange={
                                        handleChange
                                    }
                                />

                            </div>

                        </div>
                    )}

                    {activeTab ===
                        "Documents" && (
                        <FileUpload
                            label="Birth Certificate"
                            fileName={
                                birthCertificate?.name
                            }
                            onChange={
                                setBirthCertificate
                            }
                        />
                    )}

                </div>

                <div
                    className="
                        flex
                        justify-end
                        gap-3
                        mt-6
                    "
                >
                    <Button
                        variant="secondary"
                        onClick={() =>
                            setDrawerOpen(false)
                        }
                    >
                        Cancel
                    </Button>

                    <Button>
                        Save Student
                    </Button>
                </div>

            </CrudDrawer>

        </div>
    );
};

export default StudentShowcasePage;