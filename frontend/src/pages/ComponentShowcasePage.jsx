import { useState } from "react";

import Button from "../components/ui/Button";
import Input from "../components/ui/Input";
import Select from "../components/ui/Select";
import Textarea from "../components/ui/Textarea";
import Checkbox from "../components/ui/Checkbox";
import Switch from "../components/ui/Switch";
import Card from "../components/ui/Card";
import Badge from "../components/ui/Badge";
import Loader from "../components/ui/Loader";

import ConfirmDialog from "../components/dialogs/ConfirmDialog";
import DeleteDialog from "../components/dialogs/DeleteDialog";

import CrudDrawer from "../components/crud/CrudDrawer";

const ComponentShowcasePage = () => {

    const [formData, setFormData] = useState({
        name: "",
        code: "",
        status: "active",
        description: "",
        agree: false,
        enabled: true,
    });

    const [confirmOpen, setConfirmOpen] =
        useState(false);

    const [deleteOpen, setDeleteOpen] =
        useState(false);

    const [drawerOpen, setDrawerOpen] =
        useState(false);

    const [activeTab, setActiveTab] =
        useState("Basic Info");

    const tabs = [
        "Basic Info",
        "Academic",
        "Guardian",
        "Documents",
    ];

    const handleChange = (event) => {

        const {
            name,
            value,
            type,
            checked,
        } = event.target;

        setFormData((prev) => ({
            ...prev,
            [name]:
                type === "checkbox"
                    ? checked
                    : value,
        }));
    };

    return (

        <div className="p-6 space-y-6 bg-gray-100 min-h-screen">

            <h1 className="text-3xl font-bold">
                ERP Component Playground
            </h1>

            {/* Buttons */}

            <Card title="Buttons">

                <div className="flex gap-3 flex-wrap">

                    <Button variant="primary">
                        Save
                    </Button>

                    <Button variant="secondary">
                        Cancel
                    </Button>

                    <Button variant="success">
                        Approve
                    </Button>

                    <Button variant="danger">
                        Delete
                    </Button>

                </div>

            </Card>

            {/* Inputs */}

            <Card title="Inputs">

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">

                    <Input
                        label="Building Name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                    />

                    <Input
                        label="Building Code"
                        name="code"
                        value={formData.code}
                        onChange={handleChange}
                    />

                    <Select
                        label="Status"
                        name="status"
                        value={formData.status}
                        onChange={handleChange}
                        options={[
                            {
                                value: "active",
                                label: "Active",
                            },
                            {
                                value: "inactive",
                                label: "Inactive",
                            },
                        ]}
                    />

                    <div className="md:col-span-2">

                        <Textarea
                            label="Description"
                            name="description"
                            value={formData.description}
                            onChange={handleChange}
                        />

                    </div>

                </div>

            </Card>

            {/* Checkbox & Switch */}

            <Card title="Checkbox & Switch">

                <div className="space-y-4">

                    <Checkbox
                        label="I Agree"
                        name="agree"
                        checked={formData.agree}
                        onChange={handleChange}
                    />

                    <Switch
                        label="Enabled"
                        checked={formData.enabled}
                        onChange={() =>
                            setFormData((prev) => ({
                                ...prev,
                                enabled:
                                    !prev.enabled,
                            }))
                        }
                    />

                </div>

            </Card>

            {/* Badges */}

            <Card title="Badges">

                <div className="flex gap-3">

                    <Badge variant="success">
                        Active
                    </Badge>

                    <Badge variant="danger">
                        Inactive
                    </Badge>

                    <Badge variant="warning">
                        Pending
                    </Badge>

                    <Badge variant="primary">
                        Draft
                    </Badge>

                </div>

            </Card>

            {/* Loader */}

            <Card title="Loader">

                <Loader />

            </Card>

            {/* Dialogs */}

            <Card title="Dialogs">

                <div className="flex gap-3">

                    <Button
                        onClick={() =>
                            setConfirmOpen(true)
                        }
                    >
                        Open Confirm Dialog
                    </Button>

                    <Button
                        variant="danger"
                        onClick={() =>
                            setDeleteOpen(true)
                        }
                    >
                        Open Delete Dialog
                    </Button>

                </div>

            </Card>

            {/* Drawer */}

            <Card title="Crud Drawer">

                <Button
                    onClick={() =>
                        setDrawerOpen(true)
                    }
                >
                    Open Drawer
                </Button>

            </Card>

            {/* Current Form Data */}

            <Card title="Current State">

                <pre className="bg-gray-100 p-4 rounded overflow-auto">
                    {JSON.stringify(
                        formData,
                        null,
                        2
                    )}
                </pre>

            </Card>

            {/* Confirm Dialog */}

            <ConfirmDialog
                open={confirmOpen}
                title="Activate Record"
                message="Do you want to activate this record?"
                onCancel={() =>
                    setConfirmOpen(false)
                }
                onConfirm={() => {
                    alert("Confirmed");
                    setConfirmOpen(false);
                }}
            />

            {/* Delete Dialog */}

            <DeleteDialog
                open={deleteOpen}
                onCancel={() =>
                    setDeleteOpen(false)
                }
                onDelete={() => {
                    alert("Deleted");
                    setDeleteOpen(false);
                }}
            />

            {/* Drawer */}

            <CrudDrawer
                open={drawerOpen}
                title="Add Student"
                onClose={() =>
                    setDrawerOpen(false)
                }
                tabs={tabs}
                activeTab={activeTab}
                onTabChange={setActiveTab}
            >

                <div className="space-y-4">

                    <h2 className="font-semibold">
                        {activeTab}
                    </h2>

                    <Input
                        label="Name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                    />

                    <Input
                        label="Code"
                        name="code"
                        value={formData.code}
                        onChange={handleChange}
                    />

                    <Textarea
                        label="Description"
                        name="description"
                        value={formData.description}
                        onChange={handleChange}
                    />

                </div>

            </CrudDrawer>

        </div>
    );
};

export default ComponentShowcasePage;