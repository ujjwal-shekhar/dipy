import os
import numpy as np
import numpy.testing as npt
from dipy.tracking.streamline import Streamlines
from dipy.testing.decorators import xvfb_it, use_xvfb
from dipy.utils.optpkg import optional_package
from dipy.data import DATA_DIR

fury, has_fury, setup_module = optional_package('fury')

if has_fury:
    from dipy.viz.app import horizon

skip_it = use_xvfb == 'skip'


"""
def test_simple_interaction(recording=True):

    from os.path import join as pjoin
    from fury.tests.test_ui import EventCounter
    from fury import window

    filename = "test_ui_line_slider_2d"
    recording_filename = pjoin(DATA_DIR, filename + ".log.gz")
    expected_events_counts_filename = pjoin(DATA_DIR, filename + ".pkl")

    line_slider_2d_test = ui.LineSlider2D(initial_value=-2,
                                          min_value=-5, max_value=5)
    line_slider_2d_test.center = (300, 300)

    # Assign the counter callback to every possible event.
    event_counter = EventCounter()
    event_counter.monitor(line_slider_2d_test)

    current_size = (600, 600)
    show_manager = window.ShowManager(size=current_size,
                                      title="FURY Line Slider")

    show_manager.scene.add(line_slider_2d_test)

    if recording:
        show_manager.record_events_to_file(recording_filename)
        print(list(event_counter.events_counts.items()))
        event_counter.save(expected_events_counts_filename)

    else:
        show_manager.play_events_from_file(recording_filename)
        expected = EventCounter.load(expected_events_counts_filename)
        event_counter.check_counts(expected)
"""

# we will have to skip this as creates issues with xvfb (XIO error)
@npt.dec.skipif(skip_it or not has_fury)
# @xvfb_it
def test_horizon_events():
    affine = np.diag([2., 1, 1, 1]).astype('f8')
    data = 255 * np.random.rand(150, 150, 150)
    images = [(data, affine)]
    # images = None
    from dipy.segment.tests.test_bundles import setup_module
    setup_module()
    from dipy.segment.tests.test_bundles import f1
    streamlines = f1.copy()
    tractograms = [streamlines]
    # tractograms = None

    # enable = [1, 2, 3, 4]
    # enable = [1, 2]
    enable = [1, 2, 3]

    if 1 in enable: # just close
        # Read interesting discussion here
        # Passive observer should not call AddObserver or RemoveObserver in callback.
        # https://stackoverflow.com/questions/2452532/memory-allocation-in-xvfb
        fname = os.path.join(DATA_DIR, 'record_01.log.gz')

        horizon(tractograms=tractograms, images=images, pams=None,
                cluster=True, cluster_thr=5.0,
                random_colors=False, length_gt=0, length_lt=np.inf,
                clusters_gt=0, clusters_lt=np.inf,
                world_coords=True, interactive=True, out_png='tmp.png',
                recorded_events=fname)

    if 2 in enable: # just zoom

        fname = os.path.join(DATA_DIR, 'record_02.log.gz')

        horizon(tractograms=tractograms, images=images, pams=None,
                cluster=True, cluster_thr=5.0,
                random_colors=False, length_gt=0, length_lt=np.inf,
                clusters_gt=0, clusters_lt=np.inf,
                world_coords=True, interactive=True, out_png='tmp.png',
                recorded_events=fname)

    if 3 in enable: # select all centroids and expand
        # Generic Warning: In /work/standalone-x64-build/VTK-source/Common/Core/vtkObject.cxx, line 533
        # Passive observer should not call AddObserver or RemoveObserver in callback.

        fname = os.path.join(DATA_DIR, 'record_03.log.gz')

        horizon(tractograms=tractograms, images=images, pams=None,
                cluster=True, cluster_thr=5.0,
                random_colors=False, length_gt=0, length_lt=np.inf,
                clusters_gt=0, clusters_lt=np.inf,
                world_coords=True, interactive=True, out_png='tmp.png',
                recorded_events=fname)

    if 4 in enable: # select all centroids and expand
        # Generic Warning: In /work/standalone-x64-build/VTK-source/Common/Core/vtkObject.cxx, line 533
        # Passive observer should not call AddObserver or RemoveObserver in callback.

        fname = os.path.join(DATA_DIR, 'record_04.log.gz')

        horizon(tractograms=tractograms, images=images, pams=None,
                cluster=True, cluster_thr=5.0,
                random_colors=False, length_gt=0, length_lt=np.inf,
                clusters_gt=0, clusters_lt=np.inf,
                world_coords=True, interactive=True, out_png='tmp.png',
                recorded_events=fname)




    # exit(0)


# see comment above
@npt.dec.skipif(True)
@xvfb_it
def test_horizon_events2():

    affine = np.diag([2., 1, 1, 1]).astype('f8')
    data = 255 * np.random.rand(150, 150, 150)
    images = [(data, affine)]
    from dipy.segment.tests.test_bundles import setup_module
    setup_module()
    from dipy.segment.tests.test_bundles import f1
    streamlines = f1.copy()
    tractograms = [streamlines]
    fname = os.path.join(DATA_DIR, 'record_02.log.gz')
    horizon(tractograms, images=images, cluster=False, cluster_thr=5,
            random_colors=False, length_lt=np.inf, length_gt=0,
            clusters_lt=np.inf, clusters_gt=0,
            world_coords=True, interactive=True, recorded_events=fname)


@npt.dec.skipif(skip_it or not has_fury)
# @xvfb_it
def test_horizon():

    s1 = 10 * np.array([[0, 0, 0],
                        [1, 0, 0],
                        [2, 0, 0],
                        [3, 0, 0],
                        [4, 0, 0]], dtype='f8')

    s2 = 10 * np.array([[0, 0, 0],
                        [0, 1, 0],
                        [0, 2, 0],
                        [0, 3, 0],
                        [0, 4, 0]], dtype='f8')

    s3 = 10 * np.array([[0, 0, 0],
                        [1, 0.2, 0],
                        [2, 0.2, 0],
                        [3, 0.2, 0],
                        [4, 0.2, 0]], dtype='f8')

    print(s1.shape)
    print(s2.shape)
    print(s3.shape)

    streamlines = Streamlines()
    streamlines.append(s1)
    streamlines.append(s2)
    streamlines.append(s3)

    tractograms = [streamlines]
    images = None

    horizon(tractograms, images=images, cluster=True, cluster_thr=5,
            random_colors=False, length_lt=np.inf, length_gt=0,
            clusters_lt=np.inf, clusters_gt=0,
            world_coords=True, interactive=False)

    affine = np.diag([2., 1, 1, 1]).astype('f8')

    data = 255 * np.random.rand(150, 150, 150)

    images = [(data, affine)]

    horizon(tractograms, images=images, cluster=True, cluster_thr=5,
            random_colors=False, length_lt=np.inf, length_gt=0,
            clusters_lt=np.inf, clusters_gt=0,
            world_coords=True, interactive=False)

    tractograms = []
    horizon(tractograms, images=images, cluster=True, cluster_thr=5,
            random_colors=False, length_lt=np.inf, length_gt=0,
            clusters_lt=np.inf, clusters_gt=0,
            world_coords=True, interactive=False)


if __name__ == '__main__':

    test_horizon_events()
    # test_horizon_events2()
    test_horizon()


