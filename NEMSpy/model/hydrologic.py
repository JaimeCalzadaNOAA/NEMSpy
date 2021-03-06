from . import Model, ModelType, ModelVerbosity


class HydrologicalModel(Model):
    """
    abstract implementation of a generic hydrological modeling system
    """

    def __init__(self, processes: int, verbosity: ModelVerbosity):
        super().__init__(ModelType.HYDROLOGICAL, processes, verbosity)


class NWM(HydrologicalModel):
    """
    National Water Model
    https://water.noaa.gov/about/nwm
    """

    def __init__(self, processes: int, verbosity: ModelVerbosity):
        super().__init__(processes, verbosity)
